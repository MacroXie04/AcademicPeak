import axios from 'axios';
import { Subject, Unit } from '../types';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
});

export const getSubjects = async () => {
  const response = await api.get<Subject[]>('/subjects/');
  return response.data;
};

export const getSubject = async (id: number) => {
  const response = await api.get<Subject>(`/subjects/${id}/`);
  return response.data;
};

export const createSubject = async (data: Partial<Subject>) => {
  const response = await api.post<Subject>('/subjects/', data);
  return response.data;
};

export const getUnit = async (id: number) => {
  const response = await api.get<Unit>(`/units/${id}/`);
  return response.data;
};

export const createUnit = async (data: Partial<Unit>) => {
  const response = await api.post<Unit>('/units/', data);
  return response.data;
};

export const updateUnit = async (id: number, data: Partial<Unit>) => {
  const response = await api.put<Unit>(`/units/${id}/`, data);
  return response.data;
};

