import "./Square.css";

function Square({ corAtual }) {
  return (
    <div
      className="square-container"
      style={{ backgroundColor: corAtual }}
    ></div>
  );
}
export default Square;
