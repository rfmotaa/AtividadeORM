package Exercicio5;

import jakarta.persistence.DiscriminatorValue;
import jakarta.persistence.Entity;

@Entity
@DiscriminatorValue("JURIDICO")
public class ClienteJuridico extends Cliente {

    private String cnpj;

    public ClienteJuridico() {}

    public ClienteJuridico(String nome, String email, String cnpj) {
        super(nome, email);
        this.cnpj = cnpj;
    }

    // Getters e setters
    public String getCnpj() { return cnpj; }
    public void setCnpj(String cnpj) { this.cnpj = cnpj; }

    @Override
    public String toString() {
        return super.toString() + ", cnpj='" + cnpj + '\'';
    }
}
