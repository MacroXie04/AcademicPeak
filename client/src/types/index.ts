export interface Unit {
  id: number;
  subject: number;
  title: string;
  content: string;
  created_at: string;
  updated_at: string;
}

export interface Subject {
  id: number;
  title: string;
  description: string;
  units?: Unit[];
  created_at: string;
  updated_at: string;
}

