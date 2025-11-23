from .base import BaseAgent
from .weather_agent import WeatherAgent
from .places_agent import PlacesAgent
from ..services.geocoding_service import GeocodingService
from ..models.schemas import TourismQueryRequest, TourismQueryResponse
from ..utils.exceptions import PlaceNotFoundException

class TourismAgent(BaseAgent):
    def __init__(self):
        self.geocoding_service = GeocodingService()
        self.weather_agent = WeatherAgent()
        self.places_agent = PlacesAgent()

    async def run(self, request: TourismQueryRequest) -> TourismQueryResponse:
        query = request.query.lower()
        place = request.place or self._extract_place(query)
        # If no place found, but query is a single word, treat it as place
        if not place and len(query.split()) == 1:
            place = query.strip()
        # Map alternate city names to canonical names for geocoding
        alt_map = {
            "bengaluru": "bangalore",
            "bangaluru": "bangalore",
            "bengalore": "bangalore",
            "mangaluru": "mangalore",
            "mysuru": "mysore",
            "madras": "chennai",
            "bombay": "mumbai",
            "calcutta": "kolkata",
            "blr": "bangalore",
            "mum": "mumbai",
            "delhi": "new delhi",
            "hyd": "hyderabad",
            "tvm": "thiruvananthapuram",
            "kozhikode": "calicut",
            # Add more mappings as needed
        }
        country_capital_map = {
            "canada": "ottawa",
            "india": "new delhi",
            "australia": "canberra",
            "united states": "washington dc",
            "usa": "washington dc",
            "france": "paris",
            "germany": "berlin",
            "japan": "tokyo",
            "china": "beijing",
            "russia": "moscow",
            "brazil": "brasilia",
            "uk": "london",
            "united kingdom": "london",
            # Add more as needed
        }
        place_key = place.lower().replace(' ', '')
        # First check alternate names
        place_for_geocoding = alt_map.get(place_key, place)
        # Normalize for country mapping
        country_key = place_for_geocoding.lower().replace(' ', '')
        if country_key in [k.replace(' ', '') for k in country_capital_map.keys()]:
            for k, v in country_capital_map.items():
                if country_key == k.replace(' ', ''):
                    place_for_geocoding = v
                    break
        # Fallback for states/regions
        fallback_map = {
            "maharashtra": "mumbai",
            "karnataka": "bangalore",
            "tamilnadu": "chennai",
            "tamil nadu": "chennai",
            "gujarat": "ahmedabad",
            "westbengal": "kolkata",
            "west bengal": "kolkata",
            "uttarpradesh": "lucknow",
            "uttar pradesh": "lucknow",
            "bihar": "patna",
            "rajasthan": "jaipur",
            "punjab": "chandigarh",
            "kerala": "thiruvananthapuram",
            "andhrapradesh": "hyderabad",
            "andhra pradesh": "hyderabad",
            "telangana": "hyderabad",
            "madhyapradesh": "bhopal",
            "madhya pradesh": "bhopal",
            "odisha": "bhubaneswar",
            "jharkhand": "ranchi",
            "chhattisgarh": "raipur",
            "assam": "guwahati",
            "goa": "panaji",
            "manipur": "imphal",
            "meghalaya": "shillong",
            "mizoram": "aizawl",
            "nagaland": "kohima",
            "tripura": "agartala",
            "arunachalpradesh": "itanagar",
            "arunachal pradesh": "itanagar",
            "sikkim": "gangtok",
            "uttarakhand": "dehradun",
            "himachalpradesh": "shimla",
            "himachal pradesh": "shimla",
            "canada": "ottawa",
            "india": "new delhi",
            "australia": "sydney",
            "unitedstates": "new york",
            "united states": "new york",
            "usa": "new york",
            "france": "paris",
            "germany": "berlin",
            "japan": "tokyo",
            "china": "beijing",
            "russia": "moscow",
            "brazil": "rio de janeiro",
            "uk": "london",
            "unitedkingdom": "london",
            "united kingdom": "london",
            # Add more as needed
        }
        # Only apply fallback if the extracted place is a state (not a city)
        state_names = set([
            "maharashtra", "karnataka", "tamilnadu", "tamil nadu", "gujarat", "westbengal", "west bengal",
            "uttarpradesh", "uttar pradesh", "bihar", "rajasthan", "punjab", "kerala", "andhrapradesh", "andhra pradesh",
            "telangana", "madhyapradesh", "madhya pradesh", "odisha", "jharkhand", "chhattisgarh", "assam",
            "goa", "manipur", "meghalaya", "mizoram", "nagaland", "tripura", "arunachalpradesh", "arunachal pradesh",
            "sikkim", "uttarakhand", "himachalpradesh", "himachal pradesh"
        ])
        if place_key in state_names:
            place_for_geocoding = fallback_map[place_key]
        if not place:
            return TourismQueryResponse(
                place="",
                used_agents=[],
                weather_summary=None,
                places=None,
                message="I’m not sure this place exists or I can’t find it in my data.",
                error="PLACE_NOT_FOUND"
            )
        coords = await self.geocoding_service.get_coordinates(place_for_geocoding)
        # Fallback: if no coords, try capital/major city for states/countries
        if not coords:
            fallback_map = {
                "maharashtra": "mumbai",
                "karnataka": "bangalore",
                "tamil nadu": "chennai",
                "gujarat": "ahmedabad",
                "west bengal": "kolkata",
                "uttar pradesh": "lucknow",
                "bihar": "patna",
                "rajasthan": "jaipur",
                "punjab": "chandigarh",
                "kerala": "thiruvananthapuram",
                "andhra pradesh": "hyderabad",
                "telangana": "hyderabad",
                "madhya pradesh": "bhopal",
                "odisha": "bhubaneswar",
                "jharkhand": "ranchi",
                "chhattisgarh": "raipur",
                "assam": "guwahati",
                "canada": "ottawa",
                "india": "new delhi",
                "australia": "sydney",
                "united states": "new york",
                "usa": "new york",
                "france": "paris",
                "germany": "berlin",
                "japan": "tokyo",
                "china": "beijing",
                "russia": "moscow",
                "brazil": "rio de janeiro",
                "uk": "london",
                "united kingdom": "london",
                # Add more as needed
            }
            fallback_key = place_for_geocoding.lower().replace(' ', '')
            for k, v in fallback_map.items():
                if fallback_key == k.replace(' ', ''):
                    coords = await self.geocoding_service.get_coordinates(v)
                    place_for_geocoding = v
                    break
        if not coords:
            return TourismQueryResponse(
                place=place,
                used_agents=[],
                weather_summary=None,
                places=None,
                message="I’m not sure this place exists or I can’t find it in my data.",
                error="PLACE_NOT_FOUND"
            )
        used_agents = []
        weather_summary = None
        places = None
        message_parts = []
        # If neither weather nor places are explicitly requested, return both by default
        needs_weather = self._needs_weather(query)
        needs_places = self._needs_places(query)
        if not needs_weather and not needs_places:
            needs_weather = True
            needs_places = True
        if needs_weather:
            weather_summary = await self.weather_agent.run(coords, place)
            used_agents.append("WeatherAgent")
            if weather_summary:
                message_parts.append(weather_summary)
        if needs_places:
            places = await self.places_agent.run(coords, place)
            used_agents.append("PlacesAgent")
            if places:
                message_parts.append(f"And these are the places you can go: - " + " - ".join(places))
            else:
                message_parts.append("Sorry, I couldn't find any tourist attractions for this location. Try a nearby city or check local guides.")
        if not used_agents:
            message_parts.append("I can help with weather or places to visit. Please ask about those!")
        return TourismQueryResponse(
            place=place,
            used_agents=used_agents,
            weather_summary=weather_summary,
            places=places,
            message=" ".join(message_parts),
            error=None
        )

    async def plan(self, request):
        import asyncio
        from ..models.schemas import PlanResponse, WeatherData, ForecastDay
        query = request.query.lower()
        raw_place = request.place or self._extract_place(query)
        # Intent detection per specified rules
        weather_keywords = ["weather", "temperature", "temp", "forecast", "rain", "rainfall"]
        # Planning keywords that explicitly ask for suggestions / itinerary (exclude generic travel verbs like 'going')
        planning_keywords = [
            "plan my trip", "plan", "make my trip plan", "make my trip", "help me plan", "itinerary",
            "places", "tourist", "attractions", "give places", "suggest places", "suggest attractions",
            "places there", "tourist places", "help me plan my trip"
        ]

        if request.weather is not None or request.places is not None:
            intent_weather = bool(request.weather)
            intent_places = bool(request.places)
        else:
            has_weather = any(k in query for k in weather_keywords)
            has_plan = any(k in query for k in planning_keywords)
            # Single word or just the place name entered
            place_only_query = raw_place and query.strip() == raw_place.lower().strip()
            if has_weather and not has_plan:
                # Explicit weather request only
                intent_weather = True
                intent_places = False
            elif has_plan and not has_weather:
                # Explicit planning only
                intent_weather = False
                intent_places = True
            elif has_plan and has_weather:
                # Both asked
                intent_weather = True
                intent_places = True
            elif place_only_query:
                # Only place name -> both
                intent_weather = True
                intent_places = True
            else:
                # No specification -> both
                intent_weather = True
                intent_places = True
        if not raw_place:
            return PlanResponse(
                place="",
                used_agents=[],
                weather=None,
                places=None,
                message="I’m not sure this place exists or I can’t find it in my data.",
                error="PLACE_NOT_FOUND"
            )
        # Alias normalization (with state context where useful)
        alias = {
            "bengaluru": "bangalore, karnataka",
            "bangalore": "bangalore, karnataka",
            "mangaluru": "mangalore, karnataka",
            "mysuru": "mysore, karnataka",
            "madras": "chennai, tamil nadu",
            "bombay": "mumbai, maharashtra",
            "calcutta": "kolkata, west bengal",
            "malleshwaram": "malleshwaram, bangalore, karnataka",
            "kr puram": "kr puram, bangalore, karnataka",
            "whitefield": "whitefield, bangalore, karnataka",
            "koramangala": "koramangala, bangalore, karnataka",
            "indiranagar": "indiranagar, bangalore, karnataka",
            "jayanagar": "jayanagar, bangalore, karnataka",
            "basavanagudi": "basavanagudi, bangalore, karnataka",
            "rajajinagar": "rajajinagar, bangalore, karnataka",
            "yeshwanthpur": "yeshwanthpur, bangalore, karnataka",
            "hsr layout": "hsr layout, bangalore, karnataka",
            "btm layout": "btm layout, bangalore, karnataka",
            "electronic city": "electronic city, bangalore, karnataka",
            "jp nagar": "jp nagar, bangalore, karnataka",
            "mg road": "mg road, bangalore, karnataka",
            "silk board": "silk board, bangalore, karnataka",
            "marathahalli": "marathahalli, bangalore, karnataka",
            "hebbal": "hebbal, bangalore, karnataka",
            "yelahanka": "yelahanka, bangalore, karnataka",
        }
        place_for_geocoding = alias.get(raw_place.lower(), raw_place)
        coords = await self.geocoding_service.get_coordinates(place_for_geocoding)
        if not coords:
            # Fallback remove state suffix if added
            if "," in place_for_geocoding:
                simple = place_for_geocoding.split(",")[0].strip()
                coords = await self.geocoding_service.get_coordinates(simple)
        if not coords:
            return PlanResponse(
                place=raw_place,
                used_agents=[],
                weather=None,
                places=None,
                message="I’m not sure this place exists or I can’t find it in my data.",
                error="PLACE_NOT_FOUND"
            )
        tasks = []
        agent_names = []
        if intent_weather:
            tasks.append(self.weather_agent.run(coords, raw_place))
            agent_names.append("WeatherAgent")
        if intent_places:
            tasks.append(self.places_agent.run(coords, raw_place))
            agent_names.append("PlacesAgent")
        results = await asyncio.gather(*tasks)
        weather_data = None
        places_list = None
        wi = 0
        if intent_weather:
            w = results[wi]
            wi += 1
            if w:
                forecast_objs = [ForecastDay(**day) for day in w.get("forecast", [])]
                weather_data = WeatherData(
                    current_temperature=w["current_temperature"],
                    current_rain_chance=w["current_rain_chance"],
                    summary=w["summary"],
                    forecast=forecast_objs
                )
        if intent_places:
            p = results[-1] if intent_places and intent_weather else results[wi]
            places_list = p or []
        parts = []
        if weather_data:
            parts.append(weather_data.summary)
        if places_list:
            parts.append("Places: " + ", ".join(places_list))
        message = " | ".join(parts) if parts else "Specify weather or places in your query to get details."
        return PlanResponse(
            place=raw_place,
            used_agents=agent_names,
            weather=weather_data,
            places=places_list,
            message=message,
            error=None
        )

    def _extract_place(self, query: str) -> str:
        import re
        raw_lower = query.lower()  # keep commas to allow stopping at punctuation
        query_clean = re.sub(r'[,.!?]', ' ', raw_lower)
        words = query_clean.split()
        stop_words = {"there", "here", "what", "where", "how", "when", "why", "is", "are", "was", "were",
                     "the", "a", "an", "to", "in", "at", "on", "for", "with", "about", "from",
                     "temperature", "weather", "condition", "forecast", "rain", "climate",
                     "places", "visit", "go", "going", "travel", "trip", "plan", "planning", "make", "my",
                     "show", "tell", "want", "like", "see", "know", "find", "get", "give"}
        # Run pattern on raw_lower so comma remains a boundary
        prep_pattern = r'(?:go to|going to|travel to|travelling to|headed to|heading to|make my trip plan|make my trip|make my plan|plan my trip|visit|to|in|at|about)\s+([a-zA-Z][a-zA-Z\s\-]+?)(?:\s*,|\s+what|\s+how|\s+where|\s+when|\s+is|\s*\?|$)'
        prep_match = re.search(prep_pattern, raw_lower)
        if prep_match:
            candidate = prep_match.group(1).strip()
            words_in_candidate = candidate.split()
            # Remove trailing stopwords
            while words_in_candidate and words_in_candidate[-1] in stop_words:
                words_in_candidate.pop()
            # Remove leading stopwords (e.g., 'go to london' -> 'london')
            while words_in_candidate and words_in_candidate[0] in stop_words:
                words_in_candidate.pop(0)
            if words_in_candidate:
                return ' '.join(words_in_candidate)
        original_query = re.sub(r'[,.!?]', ' ', query)
        cap_pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b'
        cap_matches = re.findall(cap_pattern, original_query)
        for cap_match in cap_matches:
            if cap_match.lower() not in {"i", "what", "where", "how", "tell", "show", "can", "please"}:
                return cap_match.lower()
        for i in range(len(words) - 1, -1, -1):
            if i >= 2:
                three_word = f"{words[i-2]} {words[i-1]} {words[i]}"
                if all(w not in stop_words for w in [words[i-2], words[i-1], words[i]]):
                    return three_word
            if i >= 1:
                two_word = f"{words[i-1]} {words[i]}"
                if all(w not in stop_words for w in [words[i-1], words[i]]):
                    return two_word
        for w in reversed(words):
            if w not in stop_words and len(w) > 2:
                return w
        return ""
    def _needs_weather(self, query: str) -> bool:
        return any(k in query for k in ["weather", "temperature", "rain", "forecast"])

    def _needs_places(self, query: str) -> bool:
        # More robust: match 'plan', 'trip', 'places', 'visit', etc.
        return any(k in query for k in ["places", "visit", "tourist", "attractions", "plan my trip", "plan", "trip"])
