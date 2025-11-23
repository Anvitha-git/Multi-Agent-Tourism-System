import { render, screen } from '@testing-library/react';
import ResponseCard from '../ResponseCard';
import { TourismQueryResponse } from '../../types/tourism';

test('renders ResponseCard with weather and places', () => {
  const response: TourismQueryResponse = {
    place: 'Bangalore',
    used_agents: ['WeatherAgent', 'PlacesAgent'],
    weather_summary: '24°C, 35% rain',
    places: ['Lalbagh', 'Palace'],
    message: 'Combined message',
    error: null,
  };
  render(<ResponseCard response={response} />);
  expect(screen.getByText(/Bangalore/)).toBeInTheDocument();
  expect(screen.getByText(/24°C/)).toBeInTheDocument();
  expect(screen.getByText(/Lalbagh/)).toBeInTheDocument();
  expect(screen.getByText(/Combined message/)).toBeInTheDocument();
});
