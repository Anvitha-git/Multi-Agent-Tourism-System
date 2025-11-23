import React from 'react';
import { PlanResponse } from '../types/tourism';

const TempIcon = () => (
  <svg width="16" height="16" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24" className="text-travel-orange">
    <path d="M12 2a2 2 0 0 0-2 2v9.172a4 4 0 1 0 4 0V4a2 2 0 0 0-2-2z" />
  </svg>
);

const RainIcon = () => (
  <svg width="16" height="16" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24" className="text-travel-blue">
    <path d="M16 13v6M8 13v6M12 15v6" />
    <path d="M6 9a6 6 0 0 1 12 0 4 4 0 0 1-.8 2.4" />
  </svg>
);

const PlaceIcon = () => (
  <svg width="16" height="16" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24" className="text-travel-blue">
    <path d="M12 22s7-6.5 7-12A7 7 0 0 0 5 10c0 5.5 7 12 7 12z" />
    <circle cx="12" cy="10" r="3" />
  </svg>
);

const ResponseCard: React.FC<{ response: PlanResponse }> = ({ response }) => {
  const placeTitle = response.place ? response.place.replace(/\b\w/g, c => c.toUpperCase()) : '';
  return (
    <div className="travel-result-card">
      <div className="flex items-center justify-between mb-2">
        <h2 className="text-xl font-semibold tracking-tight text-travel-blue">{placeTitle}</h2>
        <span className="travel-badge">{response.used_agents.join(' + ') || 'Agents'}</span>
      </div>
      {response.weather && (
        <section>
          <div className="travel-section-title"><TempIcon /> Weather Summary</div>
          <p className="text-sm text-gray-700 leading-relaxed flex items-center gap-2">
            <RainIcon /> {response.weather.summary}
          </p>
        </section>
      )}
      {response.places && response.places.length > 0 && (
        <section>
          <div className="travel-section-title"><PlaceIcon /> Places To Visit</div>
          <div className="attraction-list">
            {response.places.map((p, i) => (
              <div key={i} className="attraction-item"><span className="attraction-bullet" />{p}</div>
            ))}
          </div>
        </section>
      )}
      {response.weather && response.weather.forecast && response.weather.forecast.length > 0 && (
        <section>
          <div className="travel-section-title"><RainIcon /> 7-Day Forecast</div>
          <div className="forecast-grid">
            {response.weather.forecast.map((d, i) => (
              <div key={i} className="forecast-item">
                <span>{d.date}</span>
                <span>{d.temp_min}°C – {d.temp_max}°C</span>
                <span>Rain {d.rain_prob ?? 0}%</span>
              </div>
            ))}
          </div>
        </section>
      )}
      <div className="travel-divider" />
      <p className="text-xs text-gray-600 mt-1 leading-relaxed">{response.message}</p>
    </div>
  );
};

export default ResponseCard;
