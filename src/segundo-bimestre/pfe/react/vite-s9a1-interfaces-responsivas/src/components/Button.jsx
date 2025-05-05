import React from 'react';
import { useState } from 'react';
import './Button.scss';

function Button() {
    const [isHovering, setIsHovering] = useState(false);

    const mouseEnterElement = () => {
        setIsHovering(true);
    };

    const mouseLeaveElement = () => {
        setIsHovering(false);
    };

    return(
        <div className='button-container'>
            <button className='button' onMouseEnter={mouseEnterElement} onMouseLeave=           {mouseLeaveElement}>{isHovering ? 'Comprar agora!' : 'Você está prestes a comprar o produto!'}
            </button>
        </div>
    );
}
export default Button;
