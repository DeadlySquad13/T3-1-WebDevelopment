export class Button {
  props = {
    text: ''
  }

  constructor(parent, props) {
    this.parent = parent;
    this.props = props;
  }

  getHTML() {
    const { onClick: handleClick } = this.props;
    const { text } = this.props;
    return (`
      <button class="Button" type="button" onclick="${handleClick}">
        ${text}
      </button>
    `);
  }

  render() {
    this.parent.insertAdjacentHTML(
      'beforeend', this.getHTML()
    );
  }
}
