{
  description = "YAAICLI - Yet Another AI CLI";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        
        pythonPackages = pkgs.python312Packages;
        
        # Custom Python environment with dependencies
        pythonWithPackages = pkgs.python312.withPackages (ps: with ps; [
          google-genai
          python-dotenv
          # Additional useful packages for development
          pip
          setuptools
          wheel
        ]);

      in {
        # Development shell
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            pythonWithPackages
            # Optional: other development tools
            git
            # You can add more tools here as needed
          ];

          # Set environment variables
          PYTHONPATH = "${pythonWithPackages}/${pythonWithPackages.sitePackages}";
        };

        # Package definition (optional, for when you want to build the project)
        packages.default = pkgs.python312Packages.buildPythonApplication {
          pname = "yaaicli";
          version = "0.1.0";
          
          src = ./.;
          
          propagatedBuildInputs = with pkgs.python312Packages; [
            google-generativeai
            python-dotenv
          ];

          # This assumes you'll have a setup.py or pyproject.toml
          # Remove this section if you don't need it initially
          doCheck = false;
          
          meta = with pkgs.lib; {
            description = "Yet Another AI CLI";
            homepage = "https://github.com/glabrie/yaaicli";
            license = licenses.mit;
            maintainers = with maintainers; [ ];
          };
        };

        # Alternative: if you prefer a simple script-based approach
        packages.yaaicli-script = pkgs.writeShellScriptBin "yaaicli" ''
          #!${pkgs.bash}/bin/bash
          exec ${pythonWithPackages}/bin/python ${./yaaicli.py} "$@"
        '';
      }
    );
}
