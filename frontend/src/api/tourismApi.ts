import api from './client';
import { TourismQueryResponse, PlanResponse } from '../types/tourism';

export async function sendTourismQuery(query: string): Promise<TourismQueryResponse> {
  const resp = await api.post('/query', { query });
  return resp.data;
}

export async function planTrip(query: string): Promise<PlanResponse> {
  const resp = await api.post('/plan', { query });
  return resp.data;
}
