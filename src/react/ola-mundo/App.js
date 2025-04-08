'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'Olá, Mundo!.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Clique aqui!'
    );
  }
}

const domContainer = document.querySelector('#container');
const root = ReactDOM.createRoot(domContainer);
root.render(e(LikeButton));