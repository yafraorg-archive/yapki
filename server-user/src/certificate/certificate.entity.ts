import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class CertificateEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column('int')
  usage: number;

  @Column( 'char', { length: 10 })
  type: string;

  @Column( 'datetime' )
  expdate: Date;

  @Column( 'datetime' )
  revdate: Date;

  @Column( 'char', { length: 1024 })
  serial: string;

  @Column( 'char', { length: 1024 })
  file: string;

  @Column( 'char', { length: 1024 })
  common_name: string;

  @Column( 'text')
  distinguished_name: string;

  @Column( 'char', { length: 1024 })
  email: string;

  @Column( 'char', { length: 256 })
  owner_id: string;

  owner = relationship("DbUser", back_populates="certificate")
}