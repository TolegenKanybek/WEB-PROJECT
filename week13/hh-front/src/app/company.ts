export interface Company{
    id:number,
    name:string,
    description:Text,
    city:string,
    address:Text
}

export class LoginResponse{
    token:string;
}