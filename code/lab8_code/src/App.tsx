import React from 'react';

import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

import { Header } from 'components/Header';

import { Main } from 'pages/Main';
import { AnimeList } from 'pages/AnimeList';
import { AnimeDetails } from 'pages/AnimeDetails';

import './App.css';

export const App: React.FC = () => {
  return (
    <Router>
      <div className="App">
        <Header>
          <ul>
            <li>
              <Link to=''>Main</Link>
            </li>
            <li>
              <Link to='anime'>Anime list</Link>
            </li>
          </ul>
        </Header>
        <main>
          <Routes>
              <Route path={'anime/:id'} element={<AnimeDetails />} />
              <Route path={'anime'} element={<AnimeList />} />
              <Route path={''} element={<Main />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

