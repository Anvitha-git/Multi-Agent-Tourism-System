import React from 'react';

const features = [
  'Natural language destination + intent parsing (weather / attractions)',
  'Parallel multi-agent orchestration (Tourism, Weather, Places)',
  'Live geocoding (Nominatim) with alias & fallback normalization',
  'Current conditions + 7-day forecast (Open-Meteo API)',
  'Curated nearby attractions via Overpass (progressive radius, de-duplication)',
  'Adaptive intent logic (planning-only, weather-only, both, defaults)',
  'Responsive modern UI (Tailwind, gradient theming, travel loader)',
  'Structured responses (PlanResponse) for predictable rendering'
];

const FeaturesSection: React.FC = () => (
  <section id="features" className="mt-10 travel-card p-6 md:p-8">
    <h3 className="text-lg font-semibold tracking-wide text-travel-blue mb-4 uppercase">Features</h3>
    <ul className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm">
      {features.map(f => (
        <li key={f} className="flex items-start gap-2">
          <span className="w-1.5 h-1.5 mt-2 rounded-full bg-travel-orange flex-shrink-0" />
          <span>{f}</span>
        </li>
      ))}
    </ul>
  </section>
);

export default FeaturesSection;
