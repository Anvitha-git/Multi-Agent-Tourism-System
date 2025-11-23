import React, { useState } from 'react';
import Layout from './components/Layout';
import Hero from './components/Hero';
import FeaturesSection from './components/FeaturesSection';
import AboutSection from './components/AboutSection';
import ResponseCard from './components/ResponseCard';
import Loader from './components/Loader';
import ErrorBanner from './components/ErrorBanner';
import { PlanResponse } from './types/tourism';
import { planTrip } from './api/tourismApi';

const App: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [response, setResponse] = useState<PlanResponse | null>(null);

  const handleSubmit = async (query: string) => {
    setLoading(true);
    setError(null);
    setResponse(null);
    try {
      const res = await planTrip(query);
      setResponse(res);
      if (res.error) setError(res.message);
    } catch (e: any) {
      setError('Network error. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout>
      <Hero onSearch={handleSubmit} loading={loading} response={response} error={error} />
      <main className="travel-container mb-16 w-full">
        <div className="max-w-4xl mx-auto">
          <FeaturesSection />
          <AboutSection />
        </div>
      </main>
    </Layout>
  );
};

export default App;
