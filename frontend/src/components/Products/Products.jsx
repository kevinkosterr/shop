import {React} from 'react'
import {useQuery} from "@apollo/client";

import {getProducts} from "../../graphql/Queries";

export const Products = () => {

    const {loading, error, data} = useQuery(getProducts);

    if (loading) return <p>Products are loading...</p>;
    if (error) return <p>Oops.. Something went wrong..</p>;


    return (
        <div></div>
    )
}

