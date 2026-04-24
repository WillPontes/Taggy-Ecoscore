import ky, { Options } from "ky";

export const api = ky.create({
  prefixUrl: process.env.NEXT_PUBLIC_API_URL,
  timeout: false,
  retry: 1,
} as Options);
