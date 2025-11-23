import httpx

class PlacesService:
    async def get_places(self, coords: dict) -> list:
        # Try progressively larger radii: 5km (neighborhoods), 15km (city), 50km (region/state)
        url = "https://overpass-api.de/api/interpreter"
        queries = [
            f"""
            [out:json][timeout:25];
            node["tourism"="attraction"](around:5000,{coords['lat']},{coords['lon']});
            out 50;
            """,
            f"""
            [out:json][timeout:25];
            node["tourism"](around:15000,{coords['lat']},{coords['lon']});
            out 100;
            """,
            f"""
            [out:json][timeout:25];
            node["tourism"](around:50000,{coords['lat']},{coords['lon']});
            out 100;
            """
        ]
        all_places = []
        async with httpx.AsyncClient() as client:
            for query in queries:
                resp = await client.post(url, data=query)
                data = resp.json()
                if "elements" in data:
                    # Only include names that are ASCII (English)
                    places = [el.get("tags", {}).get("name") for el in data["elements"] if el.get("tags", {}).get("name") and el.get("tags", {}).get("name").isascii()]
                    all_places.extend(places)
                # If we found at least 5, stop searching
                if len(set(all_places)) >= 5:
                    break
            # Remove duplicates while preserving order
            unique_places = []
            seen = set()
            for p in all_places:
                if p not in seen:
                    unique_places.append(p)
                    seen.add(p)
            # Always return at most 5 places
            return unique_places[:5]
