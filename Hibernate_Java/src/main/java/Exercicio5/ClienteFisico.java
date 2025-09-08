package Exercicio5;

import jakarta.persistence.DiscriminatorValue;
import jakarta.persistence.Entity;

@Entity
@DiscriminatorValue("FISICO")
public class ClienteFisico extends Cliente {

    private String cpf;

    public ClienteFisico() {}

    public ClienteFisico(String nome, String email, String cpf) {
        super(nome, email);
        this.cpf = cpf;
    }

    // Getters e setters
    public String getCpf() { return cpf; }
    public void setCpf(String cpf) { this.cpf = cpf; }

    @Override
    public String toString() {
        return super.toString() + ", cpf='" + cpf + '\'';
    }
}
