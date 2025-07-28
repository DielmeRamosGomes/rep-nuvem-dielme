import "./Button.css" 

function Button({onClick, label}){
    
    return(
        <div className="button-container">
            <button className="button" onClick={onClick}>{label}</button>
        </div>
    );
}
export default Button;



