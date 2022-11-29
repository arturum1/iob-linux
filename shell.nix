{ pkgs ? (import <nixpkgs> {}).pkgsCross.riscv64-embedded }:
  pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    nativeBuildInputs = [ pkgs.buildPackages.dtc ];
}
