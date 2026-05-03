import ky, { Options } from "ky";

export const api = ky.create({
  prefix: import.meta.env.VITE_API_URL,
  timeout: false,
  retry: 1,
} as Options);
