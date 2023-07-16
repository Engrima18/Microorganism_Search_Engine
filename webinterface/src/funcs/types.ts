export type Result = {
    image: string;
    species: string;
    attributes: object | undefined;
    '_additional' : object | undefined;
    certainity: number | undefined;
}