import React, {Component} from 'react';
import './UserList.css'; // Importa o CSS para estilização do componente

class UserList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            users: []  // Inicializa a lista de usuários como um array vazio
        };    
    }

    // Simula a obtenção de dados de usuários ao montar o componente
    componentDidMount() {
        this.setState({users: ['Alice', 'Bob', 'Charlie', 'Roberto', 'Ana']});
    }

    // Atualiza a lista de usuários ao receber novos dados (simulado)
    componentDidUpdate(prevProps, prevState) {
        if (prevState.users !== this.state.users) {
            console.log('Usuários atualizados:', this.state.users);
        }
    }

    // Limpa dados ao desmontar o componente
    componentWillUnmount() {
        console.log('Desmontando componente, limpando dados...');
    }

    render() {
        return (
            <div className='user-list'>
                <h1>Usuários Online:</h1>
                <ul>
                    {this.state.users.map((user, index) => (
                        <li key={index}>{user}</li>
                    ))}
                </ul>
            </div>
        );
    }
}
export default UserList;