import React from 'react';
import { BrowserRouter, Route, Routes } from "react-router-dom";

import PlayerAPI from './playerapi';
import Top from './Top';

import Headers  from './headers';

import "./css/reset.css"
import './css/App.css';
import HeadCoachAPI from './headCoachapi';
import PlayerDetail from "./playerdetail"


function App(){
    return (
        <div>
            <BrowserRouter>
                <Headers />
                <Routes>
                    <Route path="/" element={<Top />} />
                    <Route path="/player-list" element={<PlayerAPI />} />
                    <Route path="/player-detail/:id" element = {<PlayerDetail />}/>
                    <Route path="/coacher-list" element={<HeadCoachAPI />}/>
                </Routes>
            </BrowserRouter>
        </div>
    );
}

export default App;