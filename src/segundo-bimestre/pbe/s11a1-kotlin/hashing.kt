package org.example

import javax.swing.JOptionPane
import org.mindrot.jbcrypt.BCrypt // Importe a biblioteca BCrypt

fun main() {
    // 1. Solicita a senha ao usuário para "registro" (definição inicial)
    val passwordToSet = JOptionPane.showInputDialog("Defina uma senha para o sistema:")
    if (passwordToSet.isNullOrEmpty()) {
        JOptionPane.showMessageDialog(null, "Senha não pode ser vazia. Encerrando.", "Erro", JOptionPane.ERROR_MESSAGE)
        return // Encerra se a senha for vazia
    }

    // 2. Hasheia a senha definida
    val hashedPassword = BCrypt.hashpw(passwordToSet, BCrypt.gensalt())

    // Em um cenário real, 'hashedPassword' seria armazenado em um banco de dados
    // Vamos simular o armazenamento aqui:
    val storedHashedPassword = hashedPassword

    JOptionPane.showMessageDialog(null, "Senha definida com sucesso! Agora, tente fazer login.", "Informação", JOptionPane.INFORMATION_MESSAGE)

    // 3. Solicita a senha para login
    val passwordAttempt = JOptionPane.showInputDialog("Digite a senha para fazer login:")
    if (passwordAttempt.isNullOrEmpty()) {
        JOptionPane.showMessageDialog(null, "Senha de login não pode ser vazia. Encerrando.", "Erro", JOptionPane.ERROR_MESSAGE)
        return // Encerra se a senha de login for vazia
    }

    // 4. Chama a função de verificação
    verificaAcesso(passwordAttempt, storedHashedPassword)
}

fun verificaAcesso(enteredPassword: String, storedHash: String) { // Corrigido o tipo de 'storedHash'
    // 1. Usa BCrypt.checkpw para comparar a senha digitada com o hash armazenado
    val isValid = BCrypt.checkpw(enteredPassword, storedHash)

    if (isValid) {
        // Conceder acesso
        JOptionPane.showMessageDialog(null, "Acesso Liberado!", "Status do Acesso", JOptionPane.INFORMATION_MESSAGE)
    } else {
        // Mostrar mensagem de erro
        JOptionPane.showMessageDialog(null, "Acesso Negado!", "Status do Acesso", JOptionPane.ERROR_MESSAGE)
    }
}


