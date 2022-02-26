import React from 'react';
import { BrowserRouter, Route, Routes } from "react-router-dom";

import PlayerAPI from './playerapi';
import Top from './Top';

import Headers  from './headers';

import './css/App.css';


function App(){
    return (
        <div>
            <BrowserRouter>
                <Headers />
                <Routes>
                    <Route path="/" element={<Top />} />
                    <Route path="/player-list" element={<PlayerAPI />} />
                </Routes>
            </BrowserRouter>
        </div>
    );
}

export default App;