export interface IUser {
    username: string;
    first_name: string;
    last_name: string;
    email: string;
    is_superuser: boolean;
    permissions: string[];
}
