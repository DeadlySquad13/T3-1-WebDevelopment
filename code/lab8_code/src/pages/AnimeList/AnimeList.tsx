import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

export type Anime = {
  pk: string;
  title: string;
  poster: string;
  description: string;
}

export const AnimeList: React.FC = () => {
    const [animeInstances, setAnimeInstances] = useState<Anime[]>([]);

    const fetchAnimeInstances = () => {
      fetch(
        `http://localhost:8000/anime/`,
        {
          method: "GET"
        }
        )
      .then((response) => {
          return response.json();
        })
      .then((result) => {
          setAnimeInstances(result as Anime[]);
        })
      .catch((err) => {
        console.error(`Unsucessful fetch!`, err);
        });
    }

    useEffect(() => {
        fetchAnimeInstances();
    }, []);


    return (
      <div>
        <ul>
          {
            animeInstances.map((anime) => (
                <li key={anime.pk}>
                  <Link to={"/anime/" + anime.pk.toString()}>
                    {anime.title}
                  </Link>
                </li>
              ))
          }
        </ul>
      </div>
    );
}

