export interface TourismQueryResponse {
  place: string;
  used_agents: string[];
  weather_summary?: string | null;
  places?: string[] | null;
  message: string;
  error?: string | null;
}

export interface ForecastDay {
  date: string;
  temp_max: number;
  temp_min: number;
  rain_prob?: number;
}

export interface WeatherData {
  current_temperature: number;
  current_rain_chance: number;
  summary: string;
  forecast: ForecastDay[];
}

export interface PlanResponse {
  place: string;
  used_agents: string[];
  weather?: WeatherData | null;
  places?: string[] | null;
  message: string;
  error?: string | null;
}
