import React from 'react';
import styled from 'styled-components';

import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

import { Header } from 'components/Header';
import { Li } from 'components/Li';

import { Main } from 'pages/Main';
import { AnimeList } from 'pages/AnimeList';
import { AnimeDetails } from 'pages/AnimeDetails';

import './App.css';

const MainBlock = styled.main`
  display: flex;
  justify-content: center;
`


export const App: React.FC = () => {
  return (
    <Router>
      <div className="App">
        <Header>
          <ul>
            <Li>
              <Link to=''>Main</Link>
            </Li>
            <Li>
              <Link to='anime'>Anime list</Link>
            </Li>
          </ul>
        </Header>
        <MainBlock>
          <Routes>
              <Route path={'anime/:pk'} element={<AnimeDetails />} />
              <Route path={'anime'} element={<AnimeList />} />
              <Route path={''} element={<Main />} />
          </Routes>
        </MainBlock>
      </div>
    </Router>
  );
}

