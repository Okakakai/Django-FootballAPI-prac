import React from 'react'
import './App.css'
import PlayerAPI from './playerapi'

function App(){
    return (
        <div className="App">
            <header className="App-header">
                <PlayerAPI/> // 追加
            </header>
        </div>
    );
}

export default App;