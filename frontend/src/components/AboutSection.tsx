import React from 'react';

const AboutSection: React.FC = () => (
  <section id="about" className="mt-10 travel-card p-6 md:p-8">
    <h3 className="text-lg font-semibold tracking-wide text-travel-blue mb-4 uppercase">About</h3>
    <p className="text-sm leading-relaxed mb-4">
      This application demonstrates a multi-agent architecture for intelligent tourism planning. A parent TourismAgent interprets free-form user queries, extracting destination and intent. It selectively invokes WeatherAgent and PlacesAgent in parallel based on semantic cues (planning vs weather related expressions). The system normalizes place names, applies fallbacks for states/countries, and leverages external APIs for authoritative data. The result is a structured response combining current conditions, a 7-day forecast, and nearby attractions—returned only when relevant to the user\'s expressed intent.
    </p>
    <p className="text-sm leading-relaxed mb-2">
      Core goals: accuracy in place extraction, clarity in intent mapping, minimal latency via parallelism, and a trustworthy modern interface. The UI is intentionally concise—emphasizing discoverability without overwhelming the user.
    </p>
    <p className="text-xs text-gray-500">Data sources: Open-Meteo (weather), OpenStreetMap / Overpass (attractions), Nominatim (geocoding).</p>
  </section>
);

export default AboutSection;
