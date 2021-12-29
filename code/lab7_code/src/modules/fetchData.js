import { ajax } from './ajax.js';

export const fetchData = async (url) => {
    try {
      const response = await ajax.get(url);
      const { status, data } = response;

      if (status < 200 || status > 299) {
        throw new Error(`Bad request. Status: ${status}. Details: ${data.detail}`);
      }
      return data;
    } catch(err) {
        if (err instanceof Error) {
          console.error(err.message)
        }
    }
}

