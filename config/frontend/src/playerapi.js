import React, { useState, useEffect } from 'react';
import axios from 'axios';
import "./playerapi.css"

const PlayerAPI = () => {
    const [players, setplayers] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/players/")
            .then(res => {
                console.log("status:", res.status)
                console.log("axios-data:", res.data)
                setplayers(res.data)
            })
            .catch(err => {
                console.log("axiosGetErr", err)
            })
    }, [])

    return ( 
        <div className="player-card-list">
            <ul>
                {
                players.map(player =>
                    <li className="playercard" key={ player.id }>
                        <p className="totalvalue">{player.totalvalue}</p>
                        <img className="playerimg" src={player.playerimage} />
                        <p>{ player.playername }</p>
                    </li>
                )
                }
            </ul> 
        </div>
    )
}

export default PlayerAPI;