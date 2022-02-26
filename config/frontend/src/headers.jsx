import React from "react";
import { NavLink } from "react-router-dom";
import "./css/header.css"

export default function Headers(){

    return (
        <nav>
            <ul>
                <li>
                    <NavLink className="menu" to = "/">Top</NavLink>
                </li>
                <li>
                    <NavLink className="menu" to = "/player-list">登録選手一覧</NavLink>
                </li>
            </ul>
        </nav>
    );
}