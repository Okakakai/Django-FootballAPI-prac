import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

import "./css/reset.css"
// import "./css/playerdetail.css";

const PlayerDetail = () =>{
    const [player, setplayer] = useState([]);
    let { id } = useParams();

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/players/${ id }`) 
        .then(res => {
            console.log(res.data,id);
            setplayer(res.data);
        })
        .catch(err => {
            console.log("axiosGetErr", err);
        })
    },[])
    return (
        <div>
            <ul>
                <li>
                    <img className = "playerimg"src = { player.playerimage }/> 
                </li>
            </ul>
        </div>
    );
}


export default PlayerDetail;