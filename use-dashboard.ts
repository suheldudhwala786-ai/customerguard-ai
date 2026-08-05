import { useQuery } from "@tanstack/react-query";
import { supabase } from "@/lib/supabase";

const API_BASE = "https://iron-surging-badger.8000.dev.raccoonai.tech/api/v1";

async function fetchDashboard() {
  const { data: { session } } = await supabase.auth.getSession();
  const token = session?.access_token;
  
  const response = await fetch(`${API_BASE}/dashboard`, {
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });
  if (!response.ok) throw new Error("Failed to fetch dashboard");
  return response.json();
}

export function useDashboard() {
  return useQuery({
    queryKey: ['dashboard'],
    queryFn: fetchDashboard,
  });
}
