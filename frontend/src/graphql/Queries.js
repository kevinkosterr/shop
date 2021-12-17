import {gql} from "@apollo/client";

export const getProducts = gql`
    query {
        products {
            uid,
            image,
            title,
            description,
            price
        }
    }
`
