import React from "react";

const NavbarItem = ({href, text}) => {

    return(
        <a className="mr-5 hover:text-gray-900" href={href}>{text}</a>
    )

};

export default NavbarItem;
