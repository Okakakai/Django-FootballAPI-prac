import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import "./css/reset.css"
import "./css/playerapi.css";

const PlayerAPI = () => {
    const [players, setplayers] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/player-type/")
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
        <div className = "player-card-list" >
            <div> {
                <ul>{
                    players.filter( player =>{
                        return player.type == "FP"
                    })
                    .map(player =>
                        <li key={player.id}>
                            <Link to= {"/player-detail/" + player.id}>
                                <img className = "playerimg"src = { player.playerimage }/>  
                            </Link>
                        </li>
                    )
                } </ul>
            } </div>  
        </div >
    )
}

export default PlayerAPI;