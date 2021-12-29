export class AnimeCard {
  props = {
    title: null,
    description: null,
    poster: null
  }

  constructor(parent, children, props) {
    this.parent = parent;
    this.children = children;
    this.props = props;
  }

  getHTML() {
    const { title, description } = this.props;
    return (`
      <div class="AnimeCard">
        <h2>${title}</h2>
        <p>${description}</p>
        ${this.children.getHTML()}
      </div>
      `)
  }

  render() {
    const html = this.getHTML();
    this.parent.insertAdjacentHTML('beforeend', html);
  }
}
