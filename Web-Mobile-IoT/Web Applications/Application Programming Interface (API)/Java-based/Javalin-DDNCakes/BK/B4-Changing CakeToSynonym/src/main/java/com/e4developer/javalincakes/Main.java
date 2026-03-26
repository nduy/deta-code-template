package com.ddndeveloper.javalinsynonyms;

import io.javalin.Javalin;

public class Main {
    public static void main(String[] args) {
        Javalin app = Javalin.create().start(7777);

        app.get("/cakes", CakesController::getAllCakes);

        app.get("/cakes/:special", CakesController::getSpecialCake);
    }
}
