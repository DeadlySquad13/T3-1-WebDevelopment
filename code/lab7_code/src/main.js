import { MainPage } from './pages/MainPage/MainPage.js';

const root = document.getElementById('root');

const mainPage = new MainPage(root);
mainPage.render().then(() => {
}).catch((err) => {
  console.error(err)
});
