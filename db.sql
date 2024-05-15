-- // 4 types de relations : 
-- // <: one-to-many. E.g: users.id < posts.user_id
-- // >: many-to-one. E.g: posts.user_id > users.id
-- // -: one-to-one. E.g: users.id - user_infos.user_id
-- // <>: many-to-many. E.g: authors.id <> books.id

 CREATE TABLE `products` (
  `id` integer PRIMARY KEY,
  `products_id` varchar(255),
  `photo` varchar(255),
  `description` varchar(255),
  `litchi` varchar(255),
  `banane` varchar(255),
  `sucre_id` integer,
  `sucre_quantity` integer,
  `prix` integer
);

CREATE TABLE `users` (
  `id` integer PRIMARY KEY,
  `username` varchar(255),
  `password` varchar(255),
  `role` varchar(255)
);

CREATE TABLE `orders` (
  `id` integer PRIMARY KEY,
  `user_id` integer,
  `product_id` integer,
  `created_at` timestamp,
  `total` integer
);

CREATE TABLE `poppins` (
  `id` integer PRIMARY KEY,
  `poppins_name` varchar(255),
  `description` varchar(255),
  `poids` integer
);

ALTER TABLE `orders` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `orders` ADD FOREIGN KEY (`id`) REFERENCES `products` (`id`);

ALTER TABLE `products` ADD FOREIGN KEY (`litchi`) REFERENCES `poppins` (`poppins_name`);

ALTER TABLE `products` ADD FOREIGN KEY (`banane`) REFERENCES `poppins` (`poppins_name`);

ALTER TABLE `orders` ADD FOREIGN KEY (`product_id`) REFERENCES `products` (`sucre_id`);

ALTER TABLE `orders` ADD FOREIGN KEY (`product_id`) REFERENCES `products` (`sucre_quantity`);
