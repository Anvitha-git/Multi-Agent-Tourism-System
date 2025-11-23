import React from 'react';
import QueryForm from './QueryForm';
import ResponseCard from './ResponseCard';
import Loader from './Loader';
import ErrorBanner from './ErrorBanner';
import { PlanResponse } from '../types/tourism';

interface HeroProps {
  onSearch: (query: string) => void;
  loading?: boolean;
  response?: PlanResponse | null;
  error?: string | null;
}

const Hero: React.FC<HeroProps> = ({ onSearch, loading, response, error }) => {
  return (
    <header className="travel-container pt-20 pb-10">
      <div className="text-center mb-10">
        <h1 className="travel-heading">Plan Smarter. Travel Better.</h1>
        <p className="travel-subheading">Discover weather insights and curated attractions for any destination. Simply ask in natural language.</p>
      </div>
      <div className="max-w-3xl mx-auto travel-card p-6 md:p-8">
        <QueryForm onSubmit={onSearch} disabled={loading} />
        <p className="text-xs text-gray-500 mt-4">Try: <span className="font-medium">plan my trip to Paris</span>, <span className="font-medium">weather in Rome</span>, or just <span className="font-medium">Hyderabad</span>.</p>
        {loading && <Loader />}
        {error && <div className="mt-4"><ErrorBanner message={error} /></div>}
        {response && !error && (
          <div className="mt-6">
            <ResponseCard response={response} />
          </div>
        )}
      </div>
    </header>
  );
};

export default Hero;
