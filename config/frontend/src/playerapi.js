import React, { useState, useEffect } from 'react';
import axios from 'axios';

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
        <div>
        <ul > {
            players.map(player =>
                <li key = { player.id } > { player.playername } : { player.totalvalue } </li>
            )
        } </ul> 
            </div>
    )
}

export default PlayerAPI;