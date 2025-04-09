import { createRoot } from 'react-dom/client';
import '/src/react/react-exemplo/public/css/style.css';
import MeuApp from '/src/react/react-exemplo/componentes/MeuApp.js';
import React from 'react';

const root = createRoot(document.getElementById('container'));
root.render(
    <React.StrictMode>
        <MeuApp />
    </React.StrictMode>
);