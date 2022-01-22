import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Li } from 'components/Li';
import styled from 'styled-components';

export type Anime = {
  pk: string;
  title: string;
  poster: string;
  description: string;
}

const Ul = styled.ul`
  li {
    margin-top: 10px;
  }
`

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
        <Ul>
          {
            animeInstances.map((anime) => (
                <Li key={anime.pk} color="#282c34" hoverColor="#61dafb">
                  <Link to={"/anime/" + anime.pk.toString()}>
                    {anime.title}
                  </Link>
                </Li>
              ))
          }
        </Ul>
      </div>
    );
}

