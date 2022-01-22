import React, { useState, useEffect, useCallback } from 'react';
import { useParams } from 'react-router';
import styled from 'styled-components';

import 'App.css';

export type Anime = {
  pk: string;
  title: string;
  poster: string;
  description: string;
}

const AnimeDetailsStyled = styled.div`
  max-width: 320px;
  padding: 20px;
  display: flex;
  flex-direction: column;
`

export const AnimeDetails: React.FC = () => {
    const pk = useParams().pk;

    const [anime, setAnime] = useState<Anime | null>();

    const fetchAnime = useCallback(() => {
      if (!pk) {
        return;
      }
      fetch(
        `http://localhost:8000/anime/${pk}/`,
        {
          method: "GET"
        }
        )
      .then((response) => {
          return response.json();
        })
      .then((result) => {
          setAnime(result as Anime);
        })
      .catch((err) => {
        console.error(`Unsucessful fetch!`, err);
        });
    }, [pk]);

    useEffect(() => {
        fetchAnime();
    }, [fetchAnime]);

    return anime
      ? (
        <AnimeDetailsStyled>
          <h1>{anime.title}</h1>
          <img src={anime.poster} alt={`poster of ${anime.title}`} />
          <span>{anime.description}</span>
        </AnimeDetailsStyled>
        )
      : <span>loading</span>
}

