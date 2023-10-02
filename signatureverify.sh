#!/bin/bash

current_date=$(date +%Y-%m-%d)
base_directory="/var/log/LogSignatures"
daily_directory="$base_directory/$current_date"
if [ ! -d "$daily_directory" ]; then
  mkdir -p "$daily_directory"
fi

sign_log_file() {
  if [ $# -ne 3 ]; then
    echo "Usage: $0 sign <log_file> <private_key_file> <passphrase>"
    exit 1
  fi
  log_file="$1"
  private_key="$2"
  passphrase="$3"
  signature_file="$log_file.sig"
  hex_signature_file="$log_file.imza"
  if [ ! -f "$log_file" ]; then
    echo "Log file '$log_file' does not exist."
    exit 1
  fi
  openssl dgst -sha256 -sign "$private_key" -out "$signature_file" -passin pass:"$passphrase" "$log_file"
  if [ $? -eq 0 ]; then
    xxd -p -c 256 "$signature_file" > "$hex_signature_file"
    cp $hex_signature_file $daily_directory
    filename=$(basename "$log_file")
    echo "[+]Signature Signed Successfully: $daily_directory/$filename.imza"
    rm $signature_file
  else
    echo "Failed to create a signature."
    exit 1
  fi
}
verify_signature() {
  if [ $# -ne 4 ]; then
    echo "Usage: $0 verify <log_file> <public_key_file> <signature_file> <passphrase>"
    exit 1
  fi
  log_file="$1"
  public_key="$2"
  signature_file="$3"
  passphrase="$4"
  hex_signature_file="$signature_file.hex"
  if [ ! -f "$log_file" ] || [ ! -f "$hex_signature_file" ]; then
    echo "Log file or hexadecimal signature file missing."
    exit 1
  fi
  xxd -r -p "$hex_signature_file" > "$signature_file"
  openssl dgst -sha256 -verify "$public_key" -signature "$signature_file" "$log_file"
  if [ $? -eq 0 ]; then
    echo "Signature is valid."
  else
    echo "Signature is invalid."
    exit 1
  fi
}
if [ $# -lt 2 ]; then
  echo "Usage: $0 <action> [<log_file> [<key_file> [<signature_file> [<passphrase>]]]]"
  exit 1
fi
action="$1"
if [ "$action" == "sign" ]; then
  sign_log_file "${@:2}"
elif [ "$action" == "verify" ]; then
  verify_signature "${@:2}"
else
  echo "Invalid action. Use 'sign' or 'verify'."
  exit 1
fi
