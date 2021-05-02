module CartasPoker where

type Palo = String
type Valor = String
type Carta = (Palo, Valor)
type Cartas = [Carta]

baraja_incompleta::Cartas
baraja_incompleta = [("picas","A"),("picas","9"),("corazones","K"),("treboles","5"),("diamantes","Q"),("treboles","10"),("corazones","K")]

buscar_carta::Cartas->Carta->String
buscar_carta [] carta = "No esta"
buscar_carta ((p,v): cs) (p_buscado,v_buscado)
    | p == p_buscado && v == v_buscado = "Si esta"
    | otherwise = buscar_carta cs (p_buscado,v_buscado)

retornar_valor_real::Carta->Int
retornar_valor_real (palo,valor)
                | valor == "A" = 1
                | valor == "J" = 11
                | valor == "Q" = 12
                | valor == "K" = 13